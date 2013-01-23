var scrollPos; 
function get_num_scroll(){
    if (typeof window.pageYOffset != 'undefined')    //针对Netscape 浏览器
    { 
        scrollPos = window.pageYOffset; 
    } 
    else if (typeof document.compatMode != 'undefined' &&   document.compatMode != 'BackCompat')
    { 
        scrollPos = document.documentElement.scrollTop; 
    } 
    else if (typeof document.body != 'undefined') 
    { 
        scrollPos = document.body.scrollTop; 
    } 
    console.log("scrollPos:"+scrollPos);
    if(scrollPos>150){
        $("#scroll_top").show();
    }
    else{$("#scroll_top").hide();}
}
window.onscroll=function(){get_num_scroll();};