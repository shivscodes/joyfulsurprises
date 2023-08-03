// Handle the Thumbnail Image click

function updateLargeImage(imageUrl) {
  var largeImage = document.getElementById("largeImage");
  largeImage.src = imageUrl;
  largeImage.alt = imageUrl;
}

// Get all price-tags using querySelectorAll
const priceTags = document.querySelectorAll(".price-tag");

// Loop through each price-tag to calculate and fill the discount percentage
priceTags.forEach((priceTag) => {
  const discountedPriceElement = priceTag.querySelector(".discounted-price");
  const actualPriceElement = priceTag.querySelector(".actual-price");
  const discountPercentageElement = priceTag.querySelector(
    ".discount-percentage"
  );

  // Convert the prices to numbers for calculations
  const discountedPrice = parseInt(discountedPriceElement.textContent);
  const actualPrice = parseInt(actualPriceElement.textContent);

  // Calculate the discount percentage
  const discountPercentage =
    ((actualPrice - discountedPrice) / actualPrice) * 100;

  // Update the content of the discount-percentage span
  discountPercentageElement.textContent = `${discountPercentage.toFixed(2)}%`;
});

// Handle the favorite click on the product display page
function handleFavoriteClick(icon) {
  var previousState = icon.classList.contains("fa-regular")
    ? "fa-regular"
    : "fa-solid";
  // Get the product ID from the parent element's data attribute
  var productId = icon.parentNode.parentNode.dataset.productId;

  icon.classList.toggle("fa-solid");
  icon.classList.toggle("fa-regular");

  var flashCard = document.createElement("div");
  flashCard.classList.add("flash-card");

  var flashCardText = document.createElement("p");

  if (previousState === "fa-regular") {
    flashCardText.textContent = "Added to Wishlist" + "  " + productId;
  } else {
    flashCardText.textContent = "Removed from Wishlist" + "  " + productId;
  }

  flashCard.appendChild(flashCardText);
  document.body.appendChild(flashCard);

  setTimeout(function () {
    document.body.removeChild(flashCard);
  }, 3000);
}

// #######################################################
// Images Preview
// JavaScript for handling image preview and removal
function handleImagePreview(input) {
  if (input.files) {
    const containerId = input.id + '_preview';
    const container = document.getElementById(containerId);
    container.innerHTML = ''; // Clear previous previews

    for (let i = 0; i < input.files.length; i++) {
      const reader = new FileReader();
      const img = document.createElement('img');
      img.className = 'custom-image-preview';

      // Create a container div for each image
      const imageContainer = document.createElement('div');
      imageContainer.className = 'custom-image-container';

      // Create the 'x' symbol for removal
      const removeSymbol = document.createElement('div');
      removeSymbol.className = 'custom-image-remove';
      removeSymbol.textContent = 'x';
      removeSymbol.addEventListener('click', () => removeImage(imageContainer, input, i));

      // Read the image file and set the preview
      reader.onload = function (e) {
        img.src = e.target.result;
        imageContainer.appendChild(img);
        imageContainer.appendChild(removeSymbol);
      };
      reader.readAsDataURL(input.files[i]);

      container.appendChild(imageContainer);
    }

    container.style.display = 'flex';
  }
}

function removeImage(container, input, index) {
  container.parentNode.removeChild(container); // Remove the container div (which includes image and 'x' symbol)
  input.value = ''; // Clear the selected file from the input
}

// Attach event listeners to the image inputs
const imageInputs = document.querySelectorAll('input[type="file"][accept="image/*"]:not([multiple])');
const multipleImageInputs = document.querySelectorAll('input[type="file"][accept="image/*"][multiple]');

imageInputs.forEach((input) => {
  input.addEventListener('change', () => handleImagePreview(input));
});

multipleImageInputs.forEach((input) => {
  input.addEventListener('change', () => handleImagePreview(input));
});
