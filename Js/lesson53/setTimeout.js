// JavaScript setTimeout()


// როგორც ჩანს, თქვენ მუშაობთ JavaScript კონცეფციებზე და setTimeout() 
// ფუნქცია ნახსენებია თქვენს მიმდინარე ფაილში. აქ მოცემულია მაგალითი იმისა, 
// თუ როგორ შეგიძლიათ გამოიყენოთ setTimeout() თქვენს
 
 

function setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000)); 
    const expires = "expires=" + date.toUTCString();
    document.cookie = `${name}=${value}; ${expires}; path=/`;
}

function deleteCookie(name) {
    document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/`;
}

 
setCookie(  7);
console.log( document.cookie);
 
setTimeout(() => {
    deleteCookie( );
    console.log( document.cookie);
}, 5000);  