// Switch განცხადება JavaScript-ში
// switch განცხადება გამოიყენება მრავალი პირობის შესამოწმებლად და შესაბამისი კოდის შესასრულებლად. იგი ალტერნატივაა if-else განცხადების, როცა მრავალი შემთხვევაა განსაზღვრული.


//1
switch (expression) {
    case value1:
    
      break;
    case value2:
     
      break;
    default:
      
  }
  


//2
let day = "შაბათი";

switch (day) {
  case "ორშაბათი":
    console.log("დღეს ორშაბათია.");
    break;
  case "სამშაბათი":
    console.log("დღეს სამშაბათია.");
    break;
  case "შაბათი":
    console.log("დღეს შაბათია.");
    break;
  default:
    console.log("უცნობი დღე.");
}
