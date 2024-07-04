

function Home() {
  return (
    <div>
      <header className="bg-gray-800 text-white p-4">
        <nav>
          <ul className="flex space-x-4">
            <li><a href="#">Home</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">Services</a></li>
            <li><a href="#">Contact</a></li>
          </ul>
        </nav>
      </header>
      <main className="p-4">
        <h1 className="text-3xl font-bold">Mani AgroTech</h1>
        <p className="text-black mt-4">
          Mani AgroTech Welcomes you on our website, Hope you are earning well from your farm 
          but we are here for you to provide some suggetions about your crop cultivation. We 
          recommend you to which crop you should grow in your farm for better yields. Its 
          very easy to predict which crop you should grow on the basis of your soil nutrients. 
          Just test your soil in a lab to get the required information.
        </p>
        <br />
        <h3 className="text-black mt-4">Lets Start New Journey With Mani AgroTech</h3>
        <br />
        <h2 className="text-black mt-4">Click the following button for Crop recommendation</h2>
        <form action="/Predict" className="mt-4">
          <input type="submit" className="bg-blue-500 text-white px-4 py-2" value="Predict" />
        </form>
      </main>
    </div>
  );
}

export default Home;
