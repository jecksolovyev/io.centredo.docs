Template Static Elements
========================

+---------------------------------------------------------------------------------------------------------------------------------+
|                                                          Image                                                                  |
+=================================================================================================================================+
|  `<img width='100' height='50' src='image-uuid:1abd7329-86f1-4f90-81e7-37ea26fcb3a9' hash='aaf24fa42dg42gd42sgd2s2gsd'/>`       |
+---------------------------------------------------------------------------------------------------------------------------------+
|  `<img width='100' height='50' src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKAAAABQCAY=='/>`                             |
+---------------------------------------------------------------------------------------------------------------------------------+

Hash - is a necessary attribute in order to confirm the veracity of the image during the signing flow.

| There are 2 types of images:
| 1. Image uploaded to the platform
| 2. Base64 version of image

URL is not allowed for image source! Instead please download the picture and upload to the platform using API:

.. code::

    --upload--
    POST /api/v1/template/image
    response {
        "imageUuid" : "UUID",  //UUID of image
        "src" : "string",      //src for img tag in format "image-uuid:1abd7329-86f1-4f90-81e7-37ea26fcb3a9"
        "hash": "string"       //hash of the image
    }

    --download--
    GET /api/v1/template/{uuid}/image?imageUuid={required}&envelopeUuid={optional}

| `Upload API method <newtab::../openapi/authApi.html#operation/uploadImageUsingPOST>`__
| `Download API method <newtab::../openapi/authApi.html#operation/downloadTemplateImageUsingGET>`__
