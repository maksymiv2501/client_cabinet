function openTkoModal() {
    document
        .getElementById("tkoModal")
        .classList
        .add("active");
}

function closeTkoModal() {
    document
        .getElementById("tkoModal")
        .classList
        .remove("active");
}

function filterTkoList() {

    const search = document
        .getElementById("tkoSearch")
        .value
        .toLowerCase();

    document
        .querySelectorAll(".tko-item")
        .forEach(item => {

            const text = item
                .dataset
                .search
                .toLowerCase();

            item.style.display =
                text.includes(search)
                    ? "flex"
                    : "none";
        });
}

function selectAllTko() {

    document
        .querySelectorAll(".tko-check")
        .forEach(check => {
            check.checked = true;
        });

    updateSelectedTkoCount();
}

function clearAllTko() {

    document
        .querySelectorAll(".tko-check")
        .forEach(check => {
            check.checked = false;
        });

    updateSelectedTkoCount();
}

function updateSelectedTkoCount() {

    const count = document
        .querySelectorAll(".tko-check:checked")
        .length;

    document.getElementById(
        "selectedTkoCount"
    ).textContent = count;

    document.getElementById(
        "selectedTkoText"
    ).textContent = "Обрано ТКО: " + count;
}

function applyTkoSelection() {
    updateSelectedTkoCount();
    closeTkoModal();
}

document
    .querySelectorAll(".tko-check")
    .forEach(check => {

        check.addEventListener(
            "change",
            updateSelectedTkoCount
        );
    });
    /* ===== CONTACTS POLISH ===== */
