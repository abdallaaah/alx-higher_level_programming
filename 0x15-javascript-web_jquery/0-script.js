document.addEventListener('DOMContentLoaded', function (eventtt){
    const header = document.querySelector('header');
    if (header){
        header.style.color = "#FF0000";
    }
    else{
        console.log('there is no head tag');
    }
})



