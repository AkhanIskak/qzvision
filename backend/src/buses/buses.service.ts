import {Injectable} from "@nestjs/common";
import {Repository} from "typeorm";
import {BusEntity} from "./bus.entity";
import {InjectRepository} from "@nestjs/typeorm";

@Injectable()
export class BusesService {
    constructor(
        @InjectRepository(BusEntity)
        private busesRepo: Repository<BusEntity>
    ) {
    }

    async listBuses() {
        let buses = await this.busesRepo.find();
        let groupedByRoute = {};
        buses.map(bus => {
            let routeIds = Object.keys(groupedByRoute);
            if (routeIds.length > 0 && routeIds.find(r => Number(r) === bus.routeId)) {
                groupedByRoute[String(bus.routeId)].push(bus);
            } else {
                groupedByRoute[String(bus.routeId)] = [bus];
            }
        })
        return groupedByRoute;

    }

    async updateBus(bus) {
        const foundBus = await this.busesRepo.findOne({where: {specificBusId: bus.specificBusId}})
        if (!foundBus) {
            return this.busesRepo.save(bus);
        }
        foundBus.passengerAmount = foundBus.passengerAmount + bus.passengerAmount;
        return this.busesRepo.save(foundBus);

    }
}
