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
          hideQR(decodedText);
        }).catch((err) => {
          hideQR("");
        });
      },
      (errorMessage) => {
        // window.location.href = "/report-malfunction";
      })
    .catch((err) => {
      hideQR("");
    });
  }
}).catch(err => {
  alert(err);
  hideQR("");
});

function hideQR(decodedText) {
  var form = document.querySelector('.report-malfunction-form');
  var qrcontainer = document.querySelector('.qr-code-container').style.display = 'none';
  form.classList.remove('Hidden');
  var machine_name = document.querySelector('.malfunction-name').value = decodedText;
  if (decodedText != "" && decodedText != null) {
    var malfunction_description = document.querySelector('.malfunction-description').focus();
  } else {
    var machine_name = document.querySelector('.malfunction-name').focus();
  }
}