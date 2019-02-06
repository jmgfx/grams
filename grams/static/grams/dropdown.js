/* for sidebar */

var dropdown = document.getElementsByClassName("dropdown-btn");
var i;

for (i = 0; i < dropdown.length; i++) {
    dropdown[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var dropdownContent = this.nextElementSibling;
        if (dropdownContent.style.display === "block") {
            dropdownContent.style.display = "none";
        } else {
            dropdownContent.style.display = "block";
        }
        });
}

function toggleSideBar() {
    var x = document.getElementById('side-menu');

    if (screen.width <= 400){
        if (x.style.display === 'none') {
            x.style.display = 'block';
            document.getElementById('main').style.marginLeft
            = '0px';
        } else {
            x.style.display = 'none';
            document.getElementById('main').style.marginLeft
            = '0px';
        }
    }
    
    else {
        if (x.style.display === 'none') {
            x.style.display = 'block';
            document.getElementById('main').style.marginLeft
            = '250px';
        } else {
            x.style.display = 'none';
            document.getElementById('main').style.marginLeft
            = '0px';
        }
    }
}