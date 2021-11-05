=================
Import Dictionary
=================

In order to import CSV file to dictionary user has to perform 2 steps:

1. Upload CSV file by '/api/v1/upload/dictionary-large' endpoint using TUS client (https://github.com/tus/tus-js-client)

.. code:: js

    input.addEventListener("change", function(e) {
        // Get the selected file from the input element
        var file = e.target.files[0]

        // Create a new tus upload
        new tus.Upload(file, {
            endpoint: "http://localhost:8080/api/v1/upload/dictionary-large",
            retryDelays: [0, 3000, 5000, 10000, 20000],
            metadata: {
                filename: file.name,
                filetype: file.type
            },
            headers: {
                Dictionary: dictionaryUuid,
                Mailbox: mailboxUuid,
                Authorization: Bearer ...
            },
            onError: function(error) {
                console.log("Failed because: " + error)
            },
            onProgress: function(bytesUploaded, bytesTotal) {
                var percentage = (bytesUploaded / bytesTotal * 100).toFixed(2)
                console.log(bytesUploaded, bytesTotal, percentage + "%")
            },
            onSuccess: function() {
                console.log("Download %s from %s", upload.file.name, upload.url)
            },
            onAfterResponse: async (req: HttpRequest, res: HttpResponse) => {
                if (res.getHeader('Task')) {
                  taskUuid = res.getHeader('Task');
                }
            }
        }).start();
    })

2. Approve import processing task by endpoint '/api/v1/upload/{taskUuid}' with following parameters:

|   headerFirstRow: boolean - if headers are in the first row of CSV file
|   replace: boolean - clear current records before import
