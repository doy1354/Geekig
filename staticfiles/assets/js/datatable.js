document.addEventListener("DOMContentLoaded", function() {
    // Create DataTable instances for different elements
    var allBankTable = new DataTable("#allBank", {
        "dom": '<B<t>ilp>',
        // responsive: {
        //     details: false,
        // }
    });
    var bplCompteTable = new DataTable("#bpl-compte", {
        "dom": '<B<t>ilp>',
        "order": [[0, 'desc']]
    });
    var bplVisaTable = new DataTable("#bpl-visa", {
        "dom": '<B<t>ilp>',
        "order": [[0, 'desc']]
    });
    var salesTable = new DataTable("#sales", {
        "dom": '<B<t>ilp>',
        "order": [[0, 'desc']]
    });

    // Attach click event handler to element with ID "ExportReporttoExcel"
    $(".exportcsv").on("click", function() {
        // Trigger the button click for the desired DataTable instance
        // For example, let's say you want to trigger the button click for the "allBankTable" DataTable
        allBankTable.button('.buttons-csv').trigger();
    });
    $(".exportcsv").on("click", function() {
        // Trigger the button click for the desired DataTable instance
        // For example, let's say you want to trigger the button click for the "allBankTable" DataTable
        bplCompteTable.button('.buttons-csv').trigger();
    });
    $(".exportcsv").on("click", function() {
        // Trigger the button click for the desired DataTable instance
        // For example, let's say you want to trigger the button click for the "allBankTable" DataTable
        bplVisaTable.button('.buttons-csv').trigger();
    });
    $(".exportcsv").on("click", function() {
        // Trigger the button click for the desired DataTable instance
        // For example, let's say you want to trigger the button click for the "allBankTable" DataTable
        salesTable.button('.buttons-csv').trigger();
    });
})

$(function(){
    // $('.dataTable').wrap('<div class="table-responsive"></div>');

    $('.sales-card').on('click', function(){
        $('.sales-card').removeClass('active');
        $(this).addClass('active');
    });

    if($('.dropzone').length>0){
        console.log('object');
        var previewTemplate,dropzone,dropzonePreviewNode=document.querySelector("#dropzone-preview-list");dropzonePreviewNode.id="",dropzonePreviewNode&&(previewTemplate=dropzonePreviewNode.parentNode.innerHTML,dropzonePreviewNode.parentNode.removeChild(dropzonePreviewNode),dropzone=new Dropzone(".dropzone",{url:"https://httpbin.org/post",method:"post",previewTemplate:previewTemplate,previewsContainer:"#dropzone-preview"}));
    }else {
        console.log('object');
    }
});




