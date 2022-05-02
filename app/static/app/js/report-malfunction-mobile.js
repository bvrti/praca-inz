Html5Qrcode.getCameras().then(devices => {
  if (devices && devices.length) {
    var cameraId = devices[devices.length-1].id;
    const html5QrCode = new Html5Qrcode("reader");
    html5QrCode.start(
      cameraId, 
      {
        fps: 10,
        // qrbox: { width: 200, height: 200 },
        aspectRatio: 1.0,
        rememberLastUsedCamera: true,
      },
      (decodedText, decodedResult) => {
        html5QrCode.stop().then((ignore) => {
          alert(decodedText);
        }).catch((err) => {
          //window.location.href = "/report-malfunction";
        });
      },
      (errorMessage) => {
        // window.location.href = "/report-malfunction";
      })
    .catch((err) => {
      //window.location.href = "/report-malfunction";
    });
  }
}).catch(err => {
  alert(err);
  //window.location.href = "/report-malfunction";
});
