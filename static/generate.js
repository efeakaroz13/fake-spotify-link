function generate(){
    var email = document.getElementById("email");
    var url = "https://openspotify-13.herokuapp.com/notify?email="+email.value ;
    alert("Your Link is generated!!");
    document.getElementById("email").value = url;
    document.getElementById("copier").style.display="";
    document.getElementById("genbtn").classList.add("disabled");


}



function copy() {
    let copyTextarea = document.querySelector('#email');
    copyTextarea.focus();
    copyTextarea.select();
    try {
        let successful =navigator.clipboard.writeText(copyTextarea.value);
        console.log(successful)

    } catch(err) {
        alert('Unable to copy');
    }
}
