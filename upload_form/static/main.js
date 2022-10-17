const fileSelect = document.getElementById("fileSelect"),
    fileElem = document.getElementById("fileElem"),
    fileList = document.getElementById("fileList"),
    dropbox = document.getElementById("dropZone");

// self executing function here
(function() {
  // your page initialization code here
  // the DOM will be available here

  //buttons hide toggle for better site usability
  if (document.getElementById("databaseFilesList")) {
    fileList.innerHTML = "<p>より多くのファイルを選択できます！</p>";
  } else {
    fileList.innerHTML = "<p>まだファイルが選択されていらっしゃいません。</p>";
    document.getElementById('cancelAll').classList.toggle('hide');
    document.getElementById('sendAll').classList.toggle('hide');
  }
  if (document.getElementById('fileList').innerHTML == "<p>まだファイルが選択されていらっしゃいません。</p>" || document.getElementById('fileList').innerHTML == "<p>より多くのファイルを選択できます！</p>") {
    document.getElementById('localDatabaseRegistration').classList.toggle('hide');
  }
})();

//can't understand why it is not working:
function toggle(name) {
  // document.querySelectorAll(name).classList.toggle("hide");
  // document.querySelectorAll(name).forEach(el => el.classList.toggle("hide"));
}

dropbox.addEventListener("dragenter", dragenter, false);
dropbox.addEventListener("dragover", dragover, false);
//dropbox.addEventListener("drop", drop, false);
function dragenter(e) {
  e.stopPropagation();
  e.preventDefault();
}
function dragover(e) {
  e.stopPropagation();
  e.preventDefault();
}
dropbox.addEventListener("drop", (e) => {
  if (fileElem) {
    fileElem.click();
  }
  e.preventDefault(); // prevent navigation to "#"
}, false);

fileSelect.addEventListener("click", (e) => {
  if (fileElem) {
    fileElem.click();
  }
  e.preventDefault(); // prevent navigation to "#"
}, false);

fileElem.addEventListener("change", handleFiles, false);

function formatBytes(bytes, decimals = 2) {
  if (!+bytes) return '0 Bytes'
  const k = 1024
  const dm = decimals < 0 ? 0 : decimals
  const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
  const i = Math.floor(Math.log(bytes) / Math.log(k))
  return `${parseFloat((bytes / Math.pow(k, i)).toFixed(dm))} ${sizes[i]}`
}

//handlefiles() displays the selected files on the screen without registration in the database, use it if you need to:
function handleFiles() {
  if (this.files.length) {
    fileList.innerHTML = "";
    const objectsList = document.createElement("div");
    fileList.appendChild(objectsList);
    for (let i = 0; i < this.files.length; i++) {
      const li = document.createElement("object");
      objectsList.appendChild(li);

      const img = document.createElement("embed");
      img.src = URL.createObjectURL(this.files[i]);
      img.width = 320;
      img.height = 480;
      img.onload = () => {
        URL.revokeObjectURL(this.src);
      }
      li.appendChild(img);
      const info = document.createElement("div");
      const beautifulSize = formatBytes(this.files[i].size);
      info.classList.add("filePath");
      info.innerHTML = `${this.files[i].name}: ${beautifulSize} `;
      li.appendChild(info);
      }
    const invite = document.createElement("p");
    fileList.appendChild(invite);
    invite.innerHTML = "ファイルを送る前に保留："
    document.getElementById('localDatabaseRegistration').classList.toggle('hide');
  }
}