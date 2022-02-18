let i = 0
    let images = ['https://media.cntraveler.com/photos/5fda74245344ec5351d1fca8/master/pass/AspenColorado-2020-GettyImages-956105512.jpg','https://d3rr2gvhjw0wwy.cloudfront.net/uploads/mandators/49581/file-manager/egypt-cairo.jpg','https://upload.wikimedia.org/wikipedia/commons/2/2b/NYC_Downtown_Manhattan_Skyline_seen_from_Paulus_Hook_2019-12-20_IMG_7347_FRD_%28cropped%29.jpg','https://imagesvc.meredithcorp.io/v3/mm/image?q=60&c=sc&poi=face&w=1600&h=800&url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F28%2F2017%2F02%2Feiffel-tower-paris-france-EIFFEL0217.jpg','https://media.timeout.com/images/105412063/750/422/image.jpg']
    let time = 4000
    function changeImg() {
        document.slide.src= images[i]
        if (i < images.length -1) {
            i++;
        }
        else {
            i=0;
        }

        setTimeout("changeImg()", time)
    }
    window.onload = changeImg;