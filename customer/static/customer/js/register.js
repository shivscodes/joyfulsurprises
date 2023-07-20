// check mobile number

function validateMobileNumber() {
  var mobileInput = document.getElementById("mobile_number_label");
  var mobileNumber = mobileInput.value.trim();

  // Remove non-digit characters from the input
  mobileNumber = mobileNumber.replace(/\D/g, '');

  // Check if the mobile number starts with 6 and has 10 digits
  var mobileRegex = /^6\d{0,9}$/;
  if (!mobileRegex.test(mobileNumber)) {
    mobileInput.setCustomValidity("Mobile number should start with 6 and contain 10 digits only.");
  } else {
    mobileInput.setCustomValidity("");
  }
}



const inputs = document.querySelectorAll(".field input");

inputs.forEach((input) => {
  input.addEventListener("input", () => {
    const label = input.previousElementSibling;
    label.classList.toggle("hidden", input.value !== "");
  });
});

const passwordInput = document.querySelector('input[type="password"]');
const defaultBackground = "#FFFFFF";

passwordInput.addEventListener("input", () => {
  const password = passwordInput.value;
  const strength = calculatePasswordStrength(password);
  const backgroundStyle = getColorByStrength(strength);

  passwordInput.style.background = backgroundStyle;

  // Restore default background color if password is cleared
  if (password === "") {
    passwordInput.style.background = defaultBackground;
  }
});

function calculatePasswordStrength(password) {
  if (password.length < 6) {
    return 0; // Weak
  } else if (password.length < 10) {
    return 1; // Medium
  } else {
    return 2; // Strong
  }
}

function getColorByStrength(strength) {
  switch (strength) {
    case 0: // Weak
      return "#f8d7da";
    case 1: // Medium
      return "#ffffcc";
    case 2: // Strong
      return "#d4edda";
    default:
      return defaultBackground;
  }
}




