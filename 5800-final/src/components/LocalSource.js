import React from "react";
import { Map, Marker, Popup, TileLayer } from "react-leaflet";
import { Icon } from "leaflet";
import "./local.css";
import * as parkData from "../data/skateboard-parks.json";

export const sheep = new Icon({
  iconUrl: "/richard.png",
  iconSize: [25, 25],
});

const LocalSource = () => {
  const [activePark, setActivePark] = React.useState(null);

  return (
    <div>
      <div>hello</div>
      <Map center={[49.247123, -123.1416102]} zoom={13}>
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        />
        {parkData.features.map((park) => (
          <Marker
            key={park.properties.PARK_ID}
            position={[
              park.geometry.coordinates[0],
              park.geometry.coordinates[1],
            ]}
            onClick={() => {
              setActivePark(park);
            }}
            icon={sheep}
          />
        ))}

        {activePark && (
          <Popup
            position={[
              activePark.geometry.coordinates[0],
              activePark.geometry.coordinates[1],
            ]}
            onClose={() => {
              setActivePark(null);
            }}
          >
            <div>
              <h2>{activePark.properties.NAME}</h2>
              <p>{activePark.properties.DESCRIPTIO}</p>
            </div>
          </Popup>
        )}
      </Map>
    </div>
  );
};

export default LocalSource;
