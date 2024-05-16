// var map = L.map('map').setView([35.70072333, 51.38072233], 100)
// L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
//     attribution: '&copy; OpenStreetMap contributors'
// }).addTo(map);
// var redIcon = L.divIcon({
//     className: 'leaflet-div-icon',
//     html: '<i class=" fs-1 fa-solid fa-location-dot"></i>',
//     iconSize: [30, 30],
//     iconAnchor: [15, 15]
// });
//
// var marker;
// map.on('click', function (e) {
//     if (marker) {
//         map.removeLayer(marker)
//     }
//     // let homeUrl = '/'
//     marker = L.marker(e.latlng, {icon: redIcon}).addTo(map)
//     let lat = e.latlng.lat;
//     let lng = e.latlng.lng;
//     console.log(lng, lat);
//
//     $.ajax({
//         url: homeUrl,
//         type: 'get',
//         headers: {'X-CSRFToken': "{{ csrf_token }}"},
//         data: {
//             'lat': lat,
//             'lng': lng
//         },
//         success: function (data) {
//             console.log(data)
//         }
//     });
// })


//     const information1 = document.getElementById('information-1')
//     const information2 = document.getElementById('information-2')
//     const information = document.getElementById('information')
//     // const mapbox = document.getElementById('map-box')
//     // const mapIcon = document.getElementById('mapIcon')
//     const favourite = document.getElementById('favourite-box')
// //
//     function informationShow() {
//         if (information2.style.display === "none" && information1.style.display === "flex" && favourite.style.display === 'none') {
//             information2.style.display = "flex"
//             information1.style.display = "none"
//         } else {
//             information2.style.display = "none"
//             information1.style.display = "flex"
//         }
//     }

    // function showAddress() {
    //     if (addressBox.style.display === 'none') {
    //         information.style.display = 'none'
    //         information1.style.display = "none"
    //         information2.style.display = "none"
    //         favourite.style.display = "none"
    //     } else {
    //         addressBox.style.display = 'none'
    //         information.style.display = 'block'
    //         information1.style.display = "flex"
    //         favourite.style.display = "none"
    //
    //     }
    // }



//

// var marker;
// map.on('click', function (e) {
//     if (marker) {
//         map.removeLayer(marker)
//     }
//     let homeUrl = '/'
//     marker = L.marker(e.latlng, {icon: redIcon}).addTo(map)