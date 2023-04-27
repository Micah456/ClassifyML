const fileSelectorEl = document.getElementById('file-selector')
const imgEl = document.getElementById("img")

requestBody = {}
let blobToBase64 = function(blob) {
    return new Promise( resolve=>{
      let reader = new FileReader();
      reader.onload = function() {
        let dataUrl = reader.result;
        resolve(dataUrl);
      };
      reader.readAsDataURL(blob);
    });
}

function classify(){
  console.log("classifying")
  imageFile = fileSelectorEl.files.item(0)
  console.log(imageFile)
  base64_promise = blobToBase64(imageFile)
  .then(base64 => {
    requestBody['Image'] = base64
    console.log(requestBody)
    fetch("http://127.0.0.1:5001/classify", {
        method: "post",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestBody)
    })
    .then(resp => resp.json())
    .then(data => {
      answer = data.answer
      if(answer){
        window.location.replace("http://127.0.0.1:5001/result?answer=" + answer)
      }
      else{
        alert(data.message)
      }
    })
  })
}