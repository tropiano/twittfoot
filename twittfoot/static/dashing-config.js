/* global Dashboard */

var dashboard = new Dashboard();

dashboard.addWidget('clock_widget', 'Clock');

/*
dashboard.addWidget('new_users_widget', 'Number', {
	getData: function () {
	    var self = this;
	    $.get('widgets/new_users_widget/', function(data) {
		    $.extend(self.data, data);
		});
	},
	    interval: 5000
	    });
*/
/*
dashboard.addWidget('buzzwords_widget', 'List', {
	getData: function () {
	    $.extend(this.data, {
		    title: 'Buzzwords',
			more_info: '# of times said around the office',
			updated_at: 'Last updated at 18:58',
			data: [{label: 'Exit strategy', value: 24},
			       {label: 'Web 2.0', value: 12},
			       {label: 'Turn-key', value: 2},
			       {label: 'Enterprise', value: 12},
			       {label: 'Pivoting', value: 3},
			       {label: 'Leverage', value: 10},
			       {label: 'Streamlininess', value: 4},
			       {label: 'Paradigm shift', value: 6},
			       {label: 'Synergy', value: 7}]
			});
	}
    });
*/

/*
dashboard.addWidget('current_valuation_widget', 'Number', {
	getData: function () {
	    $.extend(this.scope, {
		    title: 'Current Valuation',
			moreInfo: 'In billions',
			updatedAt: 'Last updated at 14:10',
			value: '$35',
			detail: '64%'
			});
	}
    });
*/

dashboard.addWidget('number_change_test_widget', 'Numberchange', {
	getData: function () {
	    var self = this;
	    $.extend(self.scope, {
		    title: 'Twitter Followers',
			value: 32,
			previous: 7,
			updated_at: '6.1.2015 12:40:43'
			});
	},
	color: 'steelblue',
	backgroundcolor: '#96bf48'

});

/*
dashboard.addWidget('convergence_widget', 'Graph', {
	getData: function () {
	    $.extend(this.scope, {
		    title: 'Convergence',
			value: Math.floor(Math.random() * 50) + 40,
			more_info: '',
			data: [
			       { x: 0, y: Math.floor(Math.random() * 50) + 40 }, 
			       { x: 1, y: Math.floor(Math.random() * 50) + 40 }, 
			       { x: 2, y: Math.floor(Math.random() * 50) + 40 }, 
			       { x: 3, y: Math.floor(Math.random() * 50) + 40 }, 
			       { x: 4, y: Math.floor(Math.random() * 50) + 40 }
                ]
			});
	}
    });
*/



dashboard.addWidget('weather_widget', 'Weather', {
	WOEID: 2122265
	    });


dashboard.addWidget('weather_widget', 'Weather', {
	WOEID: 12591883
            });

dashboard.addWidget('weather_widget', 'Weather', {
        WOEID: 26525168
            });
			
dashboard.addWidget('twitter_widget', 'Twitter', {
	getData: function () {
	        var self = this;
	        $.get('widgets/twitter_widget/', function(data) {
	            $.extend(self.scope, data);
	        });
	    },
	    interval: 5000
});

