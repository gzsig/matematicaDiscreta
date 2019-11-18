let input = document.querySelector('#textbox');
let answer = document.querySelector('#answer');

function calculator() {
  let expression = input.value.replace(' ', '');
  let str = '1234567890-+*/()';
  for (let i = 0; i < expression.length; i++) {
    if (!str.includes(expression[i])) {
      console.log('err');
    }
  }
  let index = 0;
  let res = calc(index, expression);
  answer.innerHTML = res;
}


function calc(index, expression) {
  
}