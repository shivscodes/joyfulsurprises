function handleFavoriteClick(icon) {
  var previousState = icon.classList.contains('fa-regular') ? 'fa-regular' : 'fa-solid';
  // Get the product ID from the parent element's data attribute
  var productId = icon.parentNode.parentNode.dataset.productId;

  icon.classList.toggle('fa-solid');
  icon.classList.toggle('fa-regular');
  
  var flashCard = document.createElement('div');
  flashCard.classList.add('flash-card');
  
  var flashCardText = document.createElement('p');
  
  if (previousState === 'fa-regular') {
    flashCardText.textContent = 'Added to Wishlist' +'  ' + productId ;
  } else {
    flashCardText.textContent = 'Removed from Wishlist'+'  ' + productId ;
  }
  
  flashCard.appendChild(flashCardText);
  document.body.appendChild(flashCard);
  
  setTimeout(function() {
    document.body.removeChild(flashCard);
  }, 3000);
  
}
