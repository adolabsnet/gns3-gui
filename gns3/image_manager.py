# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import pathlib
import glob

from gns3.qt import QtWidgets
from gns3.local_server import LocalServer
from gns3.utils.file_copy_worker import FileCopyWorker
from gns3.utils.progress_dialog import ProgressDialog


class ImageManager:

    def __init__(self):
        # Remember if we already ask the user about this image for this server
        self._asked_for_this_image = {}

    def askCopyUploadImage(self, parent, path, server, node_type):
        """
        Ask user for copying the image to the default directory or upload
        it to remote server.

        :param parent: Parent window
        :param path: File path on computer
        :param server: The server where the images should be located
        :param node_type: Remote upload endpoint
        :returns path: Final path
        """

        if server and server != "local":
            return self._uploadImageToRemoteServer(path, server, node_type)
        else:
            destination_directory = self.getDirectoryForType(node_type)
            if os.path.normpath(os.path.dirname(path)) != destination_directory:
                # the IOS image is not in the default images directory
                reply = QtWidgets.QMessageBox.question(parent,
                                                       'Image',
                                                       'Would you like to copy {} to the default images directory'.format(os.path.basename(path)),
                                                       QtWidgets.QMessageBox.Yes,
                                                       QtWidgets.QMessageBox.No)
                if reply == QtWidgets.QMessageBox.Yes:
                    destination_path = os.path.join(destination_directory, os.path.basename(path))
                    try:
                        os.makedirs(destination_directory, exist_ok=True)
                    except OSError as e:
                        QtWidgets.QMessageBox.critical(parent, 'Image', 'Could not create destination directory {}: {}'.format(destination_directory, str(e)))
                        return path
                    worker = FileCopyWorker(path, destination_path)
                    progress_dialog = ProgressDialog(worker, 'Image', 'Copying {}'.format(os.path.basename(path)), 'Cancel', busy=True, parent=parent)
                    progress_dialog.show()
                    progress_dialog.exec_()
                    errors = progress_dialog.errors()
                    if errors:
                        QtWidgets.QMessageBox.critical(parent, 'Image', '{}'.format(''.join(errors)))
                        return path
                    else:
                        path = destination_path
            return path

    def _uploadImageToRemoteServer(self, path, server, node_type):
        """
        Upload image to remote server

        :param path: File path on computer
        :param server: The server where the images should be located
        :param node_type: Image node_type
        :returns path: Final path
        """

        if node_type == 'QEMU':
            upload_endpoint = '/qemu/images'
        elif node_type == 'IOU':
            upload_endpoint = '/iou/images'
        elif node_type == 'DYNAMIPS':
            upload_endpoint = '/dynamips/images'
        else:
            raise Exception('Invalid node type')

        filename = self._getRelativeImagePath(path, node_type).replace("\\", "/")
        server.post('{}/{}'.format(upload_endpoint, filename), None, body=pathlib.Path(path), progressText="Uploading {}".format(filename), timeout=None)
        return filename

    def addMissingImage(self, filename, server, node_type):
        """
        Add a missing image to the queue of images require to be upload on remote server
        :param filename: Filename of the image
        :param server: Server where image should be uploaded
        :param node_type: Type of the image
        """

        #TODO: move to server
        return

        if self._asked_for_this_image.setdefault(server.id(), {}).setdefault(filename, False):
            return
        self._asked_for_this_image[server.id()][filename] = True

        if server.isLocal():
            return
        path = os.path.join(self.getDirectoryForType(node_type), filename)
        if os.path.exists(path):
            if self._askForUploadMissingImage(filename, server):

                if filename.endswith(".vmdk"):
                    # A vmdk file could be split in multiple vmdk file
                    search = glob.escape(path).replace(".vmdk", "-*.vmdk")
                    for file in glob.glob(search):
                        self._uploadImageToRemoteServer(file, server, node_type)

                self._uploadImageToRemoteServer(path, server, node_type)
                del self._asked_for_this_image[server.id()][filename]

    def _askForUploadMissingImage(self, filename, server):
        from gns3.main_window import MainWindow
        parent = MainWindow.instance()
        reply = QtWidgets.QMessageBox.warning(parent,
                                              'Image',
                                              '{} is missing on server {} but exist on your computer. Do you want to upload it?'.format(filename, server.url()),
                                              QtWidgets.QMessageBox.Yes,
                                              QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            return True
        return False

    def _getRelativeImagePath(self, path, node_type):
        """
        Get a path relative to images directory path
        or just filename if the path is not located inside
        image directory

        :param path: file path
        :param node_type: Type of vm
        :return: file path
        """

        if not path:
            return ""
        img_directory = self.getDirectoryForType(node_type)
        path = os.path.abspath(path)
        if os.path.commonprefix([img_directory, path]) == img_directory:
            return os.path.relpath(path, img_directory)
        return os.path.basename(path)

    def getDirectory(self):
        """
        Returns the images directory path.

        :returns: path to the default images directory
        """

        return LocalServer.instance().localServerSettings()['images_path']

    def getDirectoryForType(self, node_type):
        """
        Return the path of local directory of the images
        of a specific node_type

        :param node_type: Type of vm
        """
        if node_type == 'DYNAMIPS':
            return os.path.join(self.getDirectory(), 'IOS')
        else:
            return os.path.join(self.getDirectory(), node_type)

    @staticmethod
    def instance():
        """
        Singleton to return only on instance of ImageManager.

        :returns: instance of ImageManager
        """

        if not hasattr(ImageManager, '_instance') or ImageManager._instance is None:
            ImageManager._instance = ImageManager()
        return ImageManager._instance
