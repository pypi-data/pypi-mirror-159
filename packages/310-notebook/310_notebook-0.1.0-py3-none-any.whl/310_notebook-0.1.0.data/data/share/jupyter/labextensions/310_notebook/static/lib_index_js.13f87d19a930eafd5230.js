"use strict";
(self["webpackChunk_310_notebook"] = self["webpackChunk_310_notebook"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/mainmenu */ "webpack/sharing/consume/default/@jupyterlab/mainmenu");
/* harmony import */ var _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_1__);


const extension = {
    id: '310_notebook',
    autoStart: true,
    requires: [_jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_0__.IMainMenu],
    optional: [],
    activate: (app, mainMenu) => {
        console.log('menu2');
        // Add an application command
        const { commands } = app;
        const command = '310notebook:logout';
        commands.addCommand(command, {
            label: 'Logout 310.ai notebook panel',
            execute: () => {
                location.href = 'https://310.ai/notebook/signout';
            }
        });
        // Create a new menu
        const menu = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_1__.Menu({ commands });
        menu.title.label = '310.ai';
        // Open Zethus
        // menu.addItem({ type: 'separator' });
        menu.addItem({ command: '310notebook:logout', args: {} });
        mainMenu.addMenu(menu, { rank: 100 });
        //   // Open Logger
        //   menu.addItem({ command: 'jupyterlab-ros/logConsole:open' });
        //   menu.addItem({ type: 'separator' });
        //   // Open Settings
        //   menu.addItem({ command: 'jupyterlab-ros/settings:open' });
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (extension);


/***/ })

}]);
//# sourceMappingURL=lib_index_js.13f87d19a930eafd5230.js.map