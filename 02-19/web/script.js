btnTranslate = document.getElementById('btnTranslate')

btnTranslate.addEventListener("click", function(){
    title = document.getElementById('title');
    
    title.textContent = "register form";
    alert(title.textContent) /* aqui el texto alertado es "register form" */
})
