// ჩადგმული ციკლები (Nested Loops) JavaScript-ში
// ჩადგმული ციკლები არის ერთ ციკლში მეორის გაერთიანება. ეს ტექნიკა გამოიყენება, როცა საჭიროა მონაცემების მრავალი დონის ან სტრუქტურის დამუშავება.


// for (outer initialization; outer condition; outer update) {
//     for (inner initialization; inner condition; inner update) {
      // ჩადგმული ციკლის კოდი
//     }
//   }
  



for (let i = 1; i <= 3; i++) {
    console.log("Outer loop iteration: " + i);
    
    for (let j = 1; j <= 2; j++) {
      console.log("  Inner loop iteration: " + j);
    }
  }
  