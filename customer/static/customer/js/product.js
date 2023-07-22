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
  discountPercentageElement.textContent = `${discountPercentage.toFixed(2)}% OFF`;
});