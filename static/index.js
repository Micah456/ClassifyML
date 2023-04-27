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
    //imageURL = URL.createObjectURL(imageFile)
    //console.log(imageURL)
    //imageAsTextPromise = imageFile.text()
    //.then(imageAsText => console.log(imageAsText))
    base64_promise = blobToBase64(imageFile)
    .then(base64 => requestBody['Image'] = base64)
    fetch("http://127.0.0.1:5001/classify", {
        method: "post",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        //make sure to serialize your JSON body
        body: JSON.stringify(requestBody)
    })
    .then(resp => console.log(resp.ok))
    //Complete the code here: make it change page to result and include answer as a query param
}