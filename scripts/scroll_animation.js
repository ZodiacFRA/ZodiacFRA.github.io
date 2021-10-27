function getScrollPercent() {
    var h = document.documentElement,
    b = document.body,
    st = 'scrollTop',
    sh = 'scrollHeight';
    return (h[st]||b[st]) / ((h[sh]||b[sh]) - h.clientHeight) * 100;
}
function onScroll() {
    var y = getScrollPercent();
    var container = document.getElementById("line_container");
    console.log("--------------");
    for (var idx = 0; idx < container.children.length; idx++) {
      var tmp = y * (idx + 1);
      container.children[idx].style.height = (tmp / 4).toString() + "px";

      container.children[idx].style.top = (100 + tmp).toString() + "px";

      container.children[idx].style.webkitTransform = 'rotate('+ tmp / 7 +'deg)';
      container.children[idx].style.mozTransform    = 'rotate('+ tmp / 7 +'deg)';
      container.children[idx].style.msTransform     = 'rotate('+ tmp / 7 +'deg)';
      container.children[idx].style.oTransform      = 'rotate('+ tmp / 7 +'deg)';
      container.children[idx].style.transform       = 'rotate('+ tmp / 7 +'deg)';
    }
}
window.addEventListener('scroll', onScroll)
