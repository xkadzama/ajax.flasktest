// window.addEventListener("DOMContentLoaded", () => {
//     function req(){
//         const request = new XMLHttpRequest();
//         request.open("GET", "http://127.0.0.1:5000/api");
//         request.setRequestHeader("Content-type", "application/json; charset=utf-8");
//         request.send(); 
//         request.addEventListener("readystatechange", function() {
//             if (request.readyState === 4 && request.status == 200) {
//                 let data = JSON.parse(request.responce);
//                 console.log(data)
//             } else {
//                 console.error('Что-то пошло не так');
//             }
//         });
//     }

//     req();
// });