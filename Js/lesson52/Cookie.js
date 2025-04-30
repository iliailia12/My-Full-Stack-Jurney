function setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000)); 
    const expires = "expires=" + date.toUTCString();
    document.cookie = `${name}=${value}; ${expires}; path=/`;
}


function getCookie(name) {
    const cookies = document.cookie.split("; "); 
    for (let cookie of cookies) {
        const [key, value] = cookie.split("=");                 
        if (key === name) return value;  
    }
    return null; 
}

function deleteCookie(name) {
    document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/`;
}

setCookie("username", "Ilia", 7);  
console.log("Cookie set:", document.cookie); 

const username = getCookie("username"); 
console.log("Retrieved cookie:", username);
                                              
deleteCookie("username"); 
console.log("Cookie after deletion:", document.cookie);