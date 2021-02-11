$(document).ready(function () {
    $('a[href^="newtab::"]').not('a[class*=internal]').each(function(){
        $(this).attr('href', $(this).attr('href').replace('newtab::',''));
        $(this).attr('target', '_blank');
    });
});
