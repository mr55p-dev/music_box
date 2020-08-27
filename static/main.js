var elems = document.getElementsByClassName('card-hide-overflow');

for (let i = 0; i < elems.length; i++) {
    const element = elems[i];
    $clamp(element, {clamp: 1});
}