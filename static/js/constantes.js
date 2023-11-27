/* API sheetdb */
const APIcomments_URL = "https://sheetdb.io/api/v1";
const APIcomments_URN = "19tmb6aoa1d1v";
export const APIcomments_URI = `${APIcomments_URL}/${APIcomments_URN}`;
export const TOKEN_APIcomments = 'rhsihhd4xhdlh997npxcrd5pflq98e1yaah9wher';

export const IAs_URI = "{% static './JSON/ias.json' %}";
export const IAsType_URI = "{% static './JSON/iasType.json' %}";

export const iaType = [
   {nombre:"Arte & Creatividad",image:"{% static './media/icons/1.png' %}",iaTypeID: 1},
   {nombre:"Conversasionales",image: "{% static './media/icons/2.png' %}", iaTypeID: 2},
   {nombre:"Diseño",image: "{% static './media/icons/3.png' %}", iaTypeID: 3},
   {nombre:"Educación",image: "{% static './media/icons/4.png' %}", iaTypeID: 4},
   {nombre:"Programación",image: "{% static './media/icons/5.png' %}", iaTypeID: 5},
   {nombre:"Automatización",image: "{% static './media/icons/6.png' %}", iaTypeID: 6},
   {nombre:"Texto & Traducción",image: "{% static './media/icons/7.png' %}", iaTypeID: 7}   
];
