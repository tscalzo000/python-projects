function validateForm() {

  var name = document.getElementById('nameInput').value;
  var species = document.getElementById('speciesInput').value;
  var age = document.getElementById('ageInput').value;

  if (!name.length || !species.length || !age.length ) {
    alert('Please fill out all sections.');
    return false;
  } else if (isNaN(age)) {
    alert('Please enter a valid number for age.');
    return false;
  }
}

document.getElementById('changeColor').addEventListener('click', function() {
  var color = document.getElementById('color').value;
  document.body.style.backgroundColor = color;
});

document.getElementById('hide').addEventListener('click', function() {
  document.getElementById('main').style.display = 'none';
  document.getElementById('show').style.display = 'block';
});

document.getElementById('show').addEventListener('click', function() {
  document.getElementById('main').style.display = 'block';
  document.getElementById('show').style.display = 'none';
});
