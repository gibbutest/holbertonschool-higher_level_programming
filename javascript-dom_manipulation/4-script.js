const ul = document.querySelector('.my_list');

document.querySelector('#add_item').addEventListener('click', () => {
  const li = document.createElement('li');
  li.textContent = 'Item';

  ul.append(li);
})