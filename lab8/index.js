$(function() {
    var $from = $('.from');
    var $to = $('.to');
    var $func = $('.func');
    var $button = $('.btn');
    var $output = $('.output');
    var $stop = $('.stop');

    $button.click(function () {
        var begin = parseFloat($from.val());
        var end = parseFloat($to.val());
        const func = $func.val();
        var point = [];
        var dx = 0.2;

        var dynamic = setInterval(function () {
            for (var x = begin; x <= end; x+=0.1) {
                if (x <= end){
                    var y = eval(func);
                    point.push([x, y]);
                }
            }

            const points = [{data: point, label: func}];


            var options = {
            colors: ["#FF0000"],
             grid: {
                borderWidth: 2,
                borderColor: "#000000" }
            };

            $.plot($output, points, options);
            if(document.getElementById("oscil").checked){
                $stop.show();
                begin += dx;
                end += dx
            }
            else{
                clearInterval(dynamic);
                $stop.hide()}
            point = [];
        }, 100);

        $stop.click(function () {
            clearInterval(dynamic);

        })
    });
});