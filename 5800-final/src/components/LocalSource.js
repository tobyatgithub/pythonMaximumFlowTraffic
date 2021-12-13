import React from "react";
import {
  MapContainer,
  Marker,
  Popup,
  TileLayer,
  Polyline,
} from "react-leaflet";
import { Icon } from "leaflet";
import "./local.css";
import * as parkData from "../data/vancouver-locations.json";
import * as symboLines from "../data/vancouver-symbol";
import { Button } from "react-bootstrap";

// const positionsA = [{ B: 26, C: 34, D: 28 }];
// const positionsB = [{ A: 38, C: 29, E: 42 }];
// const positionsC = [{ A: 23, B: 25, F: 42, G: 37 }];
// const positionsD = [{ A: 30, F: 38 }];
// const positionsE = [{ B: 41, H: 38, I: 22, J: 33 }];
// const positionsF = [{ C: 48, D: 38, G: 44 }];
// const positionsG = [{ C: 34, F: 44, J: 44, K: 50 }];
// const positionsH = [{ E: 38 }];
// const positionsI = [{ E: 28, J: 23 }];
// const positionsJ = [{ E: 27, G: 41, I: 26, K: 61 }];
// const positionsK = [{ G: 47, J: 52 }];
const purpleOptions = { fillcolor: "red", color: "lime" };

const symbolNameMap = new Map();
parkData.features.map((park) =>
  symbolNameMap.set(park.symbol, park.geometry.coordinates)
);
//{ "start": "A", "end": { "B": 26, "C": 34, "D": 28 } },
const linePositions = [];
symboLines.lines.map((line1) =>
  line1.end.map((end) =>
    linePositions.push([
      symbolNameMap.get(line1.start),
      symbolNameMap.get(end.name),
      end.weight,
    ])
  )
);

export const sheep = new Icon({
  iconUrl: "/richard.png",
  iconSize: [25, 25],
});

const LocalSource = () => {
  const [activePark, setActivePark] = React.useState(null);

  const handleClick = () => {};
  console.log(symbolNameMap);

  return (
    <div>
      <Button className="button" onClick={handleClick}>
        Large button
      </Button>
      <MapContainer center={[49.247123, -123.1416102]} zoom={13}>
        {/* <Circle center={[49.247123, -123.1416102]} radius={400} color="red" /> */}
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        />
        {parkData.features.map((park) => (
          <Marker
            key={park.name}
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
        {linePositions.map((l) => (
          <Polyline
            key={1}
            pathOptions={purpleOptions}
            positions={[l[0], l[1]]}
            weight={l[2] * 0.2}
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
      </MapContainer>
    </div>
  );
};

export default LocalSource;
