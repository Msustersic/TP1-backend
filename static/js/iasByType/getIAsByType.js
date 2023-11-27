export function obtenerIAsByType(data) {

   let items = "";
   const iaTypeEndPattern =`  </ul>
      </article>`;

   if (!data) {
      console.log("la lista de IAs se encuentra vacía");
      return;
   }

   for (let i=0;i<iaType.length;i++){
      let idx = i +1;
      iaTypeStartPattern = `
         <article class="byFunction">
            <header>
               <h2>${iaType[i].nombre}</h2>
               <img src="${iaType[i].image}" width="50">
            </header>
            <ul id="iaList">`;
      items += iaTypeStartPattern
      data.forEach((item) => {
         for (let j=0;j<=item.iaTypeID[j].length;j++){
            if (item.iaTypeID[j] == idx){
               let itemPattern = `
                  < li >
                     <a href="${item.link}" target="_blank">
                     <img src="${item.image}" title="${item.nombre} alt=" ${item.nombre} site">
                  </li>`;
            }
            items += itemPattern;
         }
      });
      items += iaTypeEndPattern;
   }
   console.log(items);
   return items;
};