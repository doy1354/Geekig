$(document).ready(function () {
    updateCategoryNames();
    updateSubCategoryNames();
    // Language selector change event
    $('#languageSelector').on('change', function () {
        // Get the selected language value
        var language = $(this).val();
        // Send AJAX request to update session language
        $.ajax({
            url: '/update-session-language/',
            type: 'POST',
            data: {
                'language': language,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (data) {
                updateCategoryNames(language);
                updateSubCategoryNames(language);
            },
            error: function (xhr, status, error) {
                // Error handling
                console.error('Failed to update session language:', error);
            }
        });
    });

    // Function to update category names
    function updateCategoryNames(language) {
        $.ajax({
            url: '/get-translated-category-names/',
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                // Update category names in the DOM
                $('[data-category-id]').each(function () {
                    var categoryId = $(this).data('category-id');
                    if (data.hasOwnProperty(categoryId)) {
                        $(this).text(data[categoryId]);
                    }
                });
            },
            error: function (xhr, status, error) {
                console.error('Error fetching translated category names:', error);
            }
        });
    }
    // Function to update subcategory names
    function updateSubCategoryNames(language) {
        $.ajax({
            url: '/get-translated-subcategory-names/',
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                console.log(data);
                // Update subcategory names in the DOM
                $('[data-subcategory-id]').each(function () {
                    var subcategoryId = $(this).data('subcategory-id');
                    if (data.hasOwnProperty(subcategoryId)) {
                        $(this).text(data[subcategoryId]);
                    }
                });
            },
            error: function (xhr, status, error) {
                console.error('Error fetching translated sub-category names:', error);
            }
        });
    }

});
