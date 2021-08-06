$('form#check_url_form').submit(function(e) {
    e.preventDefault();

    $("#resp_list li").each(function() {
        $(this).removeClass("show");
        $(this).removeClass("passed");
        $(this).removeClass("failed");
    });

    var resp = $.post("/check", $('form#check_url_form').serialize())
        .done(function(res) {
            $("#resp_head").text(res.msg);

            var stats = res.stats;
            if (jQuery.isEmptyObject(stats)) {
                return;
            }

            // if (stats.url) {
            //     $("#check_for").text("Проверка сайта: " + stats.url);
            // }

            if (stats.is_safe) {

            }

            $("#ssl_check").addClass("show");
            if (stats.ssl_safe) {
                $("#ssl_check").addClass("passed");
            } else {
                $("#ssl_check").addClass("failed");
            }

            $("#reg_check").addClass("show");
            if (stats.reg_safe) {
                $("#reg_check").addClass("passed");
            } else {
                $("#reg_check").addClass("failed");
            }

            $("#test1").addClass("show");
            if (stats.test1) {
                $("#test1").addClass("passed");
            } else {
                $("#test1").addClass("failed");
            }

            $("#test2").addClass("show");
            if (stats.test2) {
                $("#test2").addClass("passed");
            } else {
                $("#test2").addClass("failed");
            }
        })
        .fail(function(res) {
            console.log($('h2#resp_head'));
            $('h2#resp_head').text("Ошибка сервера");
        });

    $('input#url').val("");
});