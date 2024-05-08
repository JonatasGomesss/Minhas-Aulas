
function calcVel() {
   var vel = Number(document.getElementById('velocidade').value)
   var result = document.getElementById('des')
   var mult = document.getElementById('aprovt')
   result.innerHTML = `sua velocidade é de ${vel}km`

   if (vel <= 60) {
    result
   } else {
    mult.innerHTML = 'voce foi multado por alta velocidade.'
   }
}