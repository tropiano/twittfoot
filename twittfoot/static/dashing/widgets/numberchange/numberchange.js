/* global $, rivets, Dashing, Dashboard */

Dashing.widgets.Numberchange = function(dashboard) {
    var self = this,
        widget;
    this.__init__ = Dashing.utils.widgetInit(dashboard, 'numberchange');
    this.row = 1;
    this.col = 1;
    this.scope = {
        setGlyphicon: function() {
            var classname;
            if(self.scope.value > self.scope.previous) {
                classname = 'glyphicon glyphicon-chevron-up'
            } else if (self.scope.value < self.scope.previous) {
                classname = 'glyphicon glyphicon-chevron-down'
            } else {
                classname = 'glyphicon glyphicon-minus'
            }
            return classname;
        }
    };
    this.getWidget = function () {
        return widget;
    };
    this.getData = function () {};
    this.interval = 10000;
};
