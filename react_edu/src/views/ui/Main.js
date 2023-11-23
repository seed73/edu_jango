import {
  Row,
  Col,
  Card,
  CardBody,
  CardTitle,
  Breadcrumb,
  BreadcrumbItem,
  Button
} from "reactstrap";

const Breadcrumbs = () => {
  return (
    <Row>
      <Col>
        {/* --------------------------------------------------------------------------------*/}
        {/* Card-1*/}
        {/* --------------------------------------------------------------------------------*/}
        {/* <Card>
        </Card> */}
        <Card className="card-user">
          <CardTitle tag="h6" className="border-bottom p-3 mb-0">
            로그인 사용자
          </CardTitle>          
              <div className="card-image">
                <img
                  alt="..."
                  src={process.env.PUBLIC_URL + "/assets/images/south_dontan.png"}
                ></img>
              </div>
              <CardBody>
                <div className="author">
                  <a href="#pablo" onClick={(e) => e.preventDefault()}>
                    <img
                      alt="..."
                      className="avatar border-gray"
                      src={process.env.PUBLIC_URL + "assets/images/face-0.jpg"}
                    ></img>
                    <h5 className="title">김교육</h5>
                  </a>
                  <p className="description">the_best_teachers</p>
                </div>
                <p className="description text-center">
                  소개문구 <br></br>
                  소개문구<br></br>
                  South Dontan
                </p>
                <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
                  <Button style={{ backgroundColor: '#4880ee', /*outline:'none',*/marginTop:'10px', border:'none'}}>
                    정보변경
                  </Button>      
                </div>
              </CardBody>
            </Card>
      </Col>
    </Row>
  );
};

export default Breadcrumbs;
