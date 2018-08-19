$(document).ready(() => {
    $('#date').datepicker({
        weekStart: 1,
        autoclose: true,
        daysOfWeekHighlighted: "0,6",
        format: "yyyy/mm/dd"
    });
});