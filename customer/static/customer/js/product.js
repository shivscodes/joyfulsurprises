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

// Images Preview
function removeImage(index) {
  var previewContainer = document.getElementById('preview-container');
  var images = previewContainer.getElementsByClassName('preview-image-container');
  previewContainer.removeChild(images[index]);
}

function previewImages() {
  var previewContainer = document.getElementById('preview-container');
  var files = document.getElementById('imageUpload').files;

  if (files.length === 0) {
    previewContainer.innerHTML = '<p>No images selected</p>';
  } else {
    for (var i = 0; i < files.length; i++) {
      var file = files[i];
      var reader = new FileReader();

      reader.onload = function (event) {
        var image = new Image();
        image.src = event.target.result;
        image.classList.add('preview-image');

        var imageContainer = document.createElement('div');
        imageContainer.classList.add('preview-image-container');
        imageContainer.appendChild(image);

        var removeIcon = document.createElement('i');
        removeIcon.classList.add('remove-icon', 'fas', 'fa-light', 'fa-times', 'fa-xs');
        removeIcon.onclick = function () {
          removeImage(Array.from(previewContainer.children).indexOf(imageContainer));
        };
        imageContainer.appendChild(removeIcon);

        previewContainer.appendChild(imageContainer);
      };

      reader.readAsDataURL(file);
    }
  }
}

var imageUpload = document.getElementById('imageUpload');
imageUpload.addEventListener('change', previewImages);