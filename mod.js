import './App.css';
import BoxData from './components/box-data';
import Footer from './components/Footer';
import Header from './components/Header';
import LineCharts from "./components/line-charts";
 
function App() {
  return (
    <div className="page-container">
        <Header />
        <main>
          <BoxData/>
          {/* <LineCharts /> */}
          <div >
          {/* <iframe   src="http://localhost:3000/d/G6Qu6vBVk/weather?orgId=1&from=-6826986978871&to=-6826961778871&theme=light&kiosk" width="100%" height="800" frameborder="0"></iframe> */}
          <iframe   src="http://localhost:3000/d/iij4S1BVz/new-dashboard?orgId=1&theme=light&kiosk" width="100%" height="800" frameborder="0"></iframe>
          </div>
        </main>
      <Footer/>
    </div>
  );
}

export default App;
