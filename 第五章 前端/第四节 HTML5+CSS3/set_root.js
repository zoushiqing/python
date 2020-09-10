(function () {
    let calc = function () {
        let docElement = docElement.documentElement
        let clientWithValue = docElement.clientWidth > 750 ? 750 : docElement.clientWidth
        docElement.style.fontSize = 20 * (clientWithValue / 750) + 'px'
    };
    calc()
    window.addEventListener('resize', calc)
})