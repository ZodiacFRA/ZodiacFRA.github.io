document.addEventListener('mousemove', (event) => {
  var x = event.clientX;
  var y = event.clientY;
  var container = document.getElementById("floating_line_container");
  var screenWidth = window.screen.width;
  for (var idx = 0; idx < container.children.length; idx++) {
    // var tmpX = x + (x * ((idx - 1) / 5));
    var tmpY = y - (y * idx / 5) - 10;
    var tmpX = x - (x * idx / 5) - 10;
    // var tmp = reRange(tmpX, 0, screenWidth, 0, 20) / 2;


    // container.children[idx].style.left = (screenWidth / 10).toString() + "px";
    container.children[idx].style.left = ((2 * x) / ((idx + 1) / 2)).toString() + "px";
    // container.children[idx].style.top = (tmpY).toString() + "px";

    // var delta = (x - screenWidth / 2);
    container.children[idx].style.height = "10px";
    // container.children[idx].style.height = (Math.abs(delta / 100)).toString() + "px";
    // container.children[idx].style.webkitTransform = 'rotate('+ tmp +'deg)';
    // container.children[idx].style.mozTransform    = 'rotate('+ tmp +'deg)';
    // container.children[idx].style.msTransform     = 'rotate('+ tmp +'deg)';
    // container.children[idx].style.oTransform      = 'rotate('+ tmp +'deg)';
    // container.children[idx].style.transform       = 'rotate('+ tmp +'deg)';
  }
});

function reRange(OldValue, OldMin, OldMax, NewMin, NewMax) {
  return (((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin
}
