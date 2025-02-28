document.addEventListener('DOMContentLoaded', function () {
    console.log("🚀 Document Loaded Successfully!");

    // Load locations when the page loads
    function onPageLoad() {
        console.log("🔄 Fetching location names...");

        $.get("http://127.0.0.1:5000/get_location_names", function (data, status) {
            console.log("✅ API Response:", data);  // Debugging: Log API response

            if (data && data.locations.length > 0) {
                var uiLocations = document.getElementById("uiLocations");
                uiLocations.innerHTML = '';  // Clear existing options

                // Add default option
                var defaultOption = new Option("Choose a Location", "");
                defaultOption.disabled = true;
                defaultOption.selected = true;
                uiLocations.appendChild(defaultOption);

                // Populate dropdown
                data.locations.forEach(function (loc) {
                    var option = new Option(loc, loc);
                    uiLocations.appendChild(option);
                });

                console.log("✅ Dropdown updated with locations.");
            } else {
                alert("⚠️ Error: No locations received from server.");
            }
        }).fail(function () {
            alert("⚠️ Failed to load locations. Check API connection.");
        });
    }

    // Function to handle Estimate Price button click
    function onClickedEstimatePrice() {
        console.log("🟢 Estimate Price button clicked!");

        // Get form values
        var sqft = document.getElementById("uiSqft").value.trim();
        var bhk = document.getElementById("uiBHK").value;
        var bathrooms = document.getElementById("uiBathrooms").value;
        var location = document.getElementById("uiLocations").value;
        var estPrice = document.getElementById("uiEstimatedPrice");
        var loading = document.getElementById("loading");

        // Validate input
        if (!sqft || !bhk || !bathrooms || !location) {
            alert("🚨 Please fill in all fields.");
            return;
        }

        console.log("📨 Sending Data:", { sqft, bhk, bathrooms, location });

        // Show loading animation (if available)
        if (loading) loading.style.display = "block";

        // Send request to Flask backend
        $.ajax({
            url: "http://127.0.0.1:5000/predict_home_price",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({
                total_sqft: parseFloat(sqft),
                bhk: parseInt(bhk),
                bath: parseInt(bathrooms),
                location: location
            }),
            success: function (response) {
                console.log("✅ Response received:", response);

                // Hide loading animation
                if (loading) loading.style.display = "none"; 

                if (response.estimated_price) {
                    estPrice.innerHTML = `<h2>Estimated Price: ₹ ${response.estimated_price.toFixed(2)} Lakh</h2>`;
                } else {
                    alert("⚠️ No price data received.");
                }
            },
            error: function (error) {
                console.error("❌ API Error:", error);
                
                // Hide loading animation
                if (loading) loading.style.display = "none"; 

                alert("⚠️ There was an error processing your request.");
            }
        });
    }

    // Attach event listener to the button properly
    document.getElementById('estimatePriceBtn').addEventListener('click', onClickedEstimatePrice);

    // Load locations when the page is ready
    onPageLoad();
});
