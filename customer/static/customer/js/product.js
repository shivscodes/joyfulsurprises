// Handle the Thumbnail Image click

function updateLargeImage(imageUrl) {
  var largeImage = document.getElementById("largeImage");
  largeImage.src = imageUrl;
  largeImage.alt = imageUrl;
}

// Get all price-tags using querySelectorAll
const priceTags = document.querySelectorAll('.price-tag');

// Loop through each price-tag to calculate and fill the discount percentage
priceTags.forEach(priceTag => {
  const discountedPriceElement = priceTag.querySelector('.discounted-price');
  const actualPriceElement = priceTag.querySelector('.actual-price');
  const discountPercentageElement = priceTag.querySelector('.discount-percentage');

  // Convert the prices to numbers for calculations
  const discountedPrice = parseInt(discountedPriceElement.textContent);
  const actualPrice = parseInt(actualPriceElement.textContent);

  // Calculate the discount percentage
  const discountPercentage = ((actualPrice - discountedPrice) / actualPrice) * 100;

  // Update the content of the discount-percentage span
  discountPercentageElement.textContent = `${discountPercentage.toFixed(2)}%`;
});


// Handle the favorite click on the product display page
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

