var express = require('express');
var router = express.Router();
var schools = ["University of Northern Iowa", "Iowa State University", "University of Iowa"]

/* GET home page. */
router.get('/', function(req, res, next) {
  //res.render('index', { title: 'Express' });
  res.send(schools);
});

module.exports = router;
