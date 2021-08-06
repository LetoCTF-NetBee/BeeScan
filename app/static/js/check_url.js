$('form#check_url_form').submit(function(e) {
    e.preventDefault();

    $("#resp_list li").each(function() {
        $(this).removeClass("show");
        $(this).removeClass("passed");
        $(this).removeClass("failed");
    });

    $("#resp_head").text("");
    $("#resp_head").removeClass("passed");
    $("#resp_head").removeClass("failed");

    $("#spinner").addClass("show");

    var resp = $.post("/check", $('form#check_url_form').serialize())
        .done(function(res) {
            console.log(res)

            $("#resp_head").text(res.msg);

            var stats = res.stats;
            if (jQuery.isEmptyObject(stats)) {
                $("#spinner").removeClass("show");
                return;
            }

            // if (stats.url) {
            //     $("#check_for").text("Проверка сайта: " + stats.url);
            // }

            if (stats.is_safe) {
                $("#resp_head").addClass("passed");
            } else {
                $("#resp_head").addClass("failed");
            }

            $("#ssl_check").addClass("show");
            if (stats.ssl_safe) {
                $("#ssl_check").addClass("passed");
            } else {
                $("#ssl_check").addClass("failed");
            }

            $("#reg_check").addClass("show");
            if (stats.reg_time_ok) {
                $("#reg_check").addClass("passed");
            } else {
                $("#reg_check").addClass("failed");
            }

            $("#no_redirect").addClass("show");
            if (stats.no_redirect) {
                $("#no_redirect").addClass("passed");
            } else {
                $("#no_redirect").addClass("failed");
            }

            $("#not_in_blacklist").addClass("show");
            if (stats.not_in_blacklist) {
                $("#not_in_blacklist").addClass("passed");
            } else {
                $("#not_in_blacklist").addClass("failed");
            }

            $("#trustued_site").addClass("show");
            if (stats.trustued_site) {
                $("#trustued_site").addClass("passed");
            } else {
                $("#trustued_site").addClass("failed");
            }

            $("#not_in_openphish").addClass("show");
            if (stats.not_in_openphish) {
                $("#not_in_openphish").addClass("passed");
            } else {
                $("#not_in_openphish").addClass("failed");
            }

            $("#domain_low").addClass("show");
            if (stats.domain_low) {
                $("#domain_low").addClass("passed");
            } else {
                $("#domain_low").addClass("failed");
            }

            // $("#no_mimic").addClass("show");
            // if (stats.no_mimic) {
            //     $("#no_mimic").addClass("passed");
            // } else {
            //     $("#no_mimic").addClass("failed");
            // }

            $("#spinner").removeClass("show");
        })
        .fail(function(res) {
            console.log($('h2#resp_head'));
            $('h2#resp_head').text("Ошибка сервера");
            $("#spinner").removeClass("show");
        });

    $('input#url').val("");
});